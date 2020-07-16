import React from 'react';
import App from 'next/app';
import Router from 'next/router';
import axios from 'axios'

import UserContext from '../components/UserContext';

const API_URL = 'http://localhost:8000/api/'

export default class MyApp extends App {
    state = {
        user: null,
        access: null,
        refresh: null,
        recipes: [],
    };

    componentDidMount = () => {

        const user = localStorage.getItem('coolapp-user');
        const access = localStorage.getItem('coolapp-token');

        if (user && access) {
            this.setState({
                user,
                access,
            });
        } else {
            Router.push('/signin');
        }

    };

    signIn = async (username, password) => {


        const tokenInfo = await this.logIn(username, password);

        // If you want to store values in localStorage, here's how

        // localStorage.setItem('coolapp-user', username);
        // localStorage.setItem('coolapp-token', tokenInfo.access);


        this.setState(
            {
                user: username,
                access: tokenInfo.access,
                refresh: tokenInfo.refresh,
            },
            () => {
                Router.push('/');
            }
        );

        const recipes = await this.fetchSnacks();

        this.setState({
            recipes
        })
    };

    signOut = () => {
        localStorage.removeItem('coolapp-user');
        localStorage.removeItem('coolapp-token');
        this.setState({
            user: null,
            access: null,
            refresh: null,
        });
        Router.push('/signin');
    };



    logIn = async (username, password) => {

        const response = await axios.post(API_URL + 'token/', { username, password });

        // TODO: handle bad credentials, unknown uses, etc.
        return response.data;

    };

    refresh = async (refreshToken) => {

        const url = API_URL + 'token/refresh/';

        const response = await axios.post(url, { refresh: refreshToken })

        console.log('refreshToken', response.data);

        this.setState({
            access: response.data.access
        })

        // Update localstorage as well if desired


        return response.data.access;
    };

    fetchSnacks = async () => {

        console.log('fetch snacks - user', this.state.user);
        if (!this.state.user) {
            return []
        }

        const accessToken = this.state.access;

        let url = API_URL + 'recipes/';

        let config = {
            headers: { 'Authorization': "Bearer " + accessToken }
        };

        let response = await axios.get(url, config);

        console.log('first try', response.status)

        if (response.status !== 200) {

            const refreshToken = this.state.refresh;

            accessToken = await this.refresh(refreshToken);

            config.headers.Authorization = "Bearer " + accessToken;

            response = await axios.get(url, config);

            console.log('try again with refreshed token', response.status)

            if (response.status == 200) {
                this.setState({ access: accessToken })
            } else {
                console.error('let user know that somethings broken')
            }
        }

        return response.data;
    }

    getRecipe = (id) => {

        if (!this.state.user) {
            return null;
        }

        return this.state.recipes.find(item => item.id == id);

        // If you needed fresh, async data fetching then do something like below
        // but inside the calling component, not here

        // useEffect(() => {

        //     (async function () {
        //         console.log('router.query.id', router.query.id);
        //         const data = await fetchSnackFresh(router.query.id)
        //         setRecipe(data)
        //     })()

        // }, [])
    }


    render() {
        const { Component, pageProps } = this.props;

        return (
            <UserContext.Provider value={{
                user: this.state.user,
                access: this.state.access,
                refresh: this.state.refresh,
                recipes: this.state.recipes,
                fetchSnacks: this.fetchSnacks,
                getRecipe: this.getRecipe,
                signIn: this.signIn,
                signOut: this.signOut
            }}>
                <Component {...pageProps} />
            </UserContext.Provider>
        );
    }
}
