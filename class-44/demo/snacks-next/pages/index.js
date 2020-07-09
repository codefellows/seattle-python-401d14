import React from 'react'
import axios from 'axios'
import Nav from '../components/Nav'
import SnackForm from '../components/SnackForm'
import SnackItem from '../components/SnackItem'
import Footer from '../components/Footer'

const url = 'https://drf-snacks-api.herokuapp.com/api/v1/snacks/';

class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            snacks: props.snacks
        }
        this.snackCreateHandler = this.snackCreateHandler.bind(this);
    }

    async snackCreateHandler(snack) {

        const response = await axios.post(url, snack);

        // decision: add the newly created to state or fetch brand new
        // let's go with option 1
        const savedSnack = response.data;

        const updatedSnacks = this.state.snacks.concat(savedSnack);

        this.setState({
            snacks: updatedSnacks
        })

        // Stretch: how can you make even snappier?
    }

    render() {
        return (
            <div className="container">
                <Nav page="home" />
                <h1>Snacks Home</h1>

                <div className="flex">

                <section className="w-1/4">
                    <div className="max-w-sm rounded overflow-hidden shadow-lg">
                        <img className="w-full" src="/Snack_Time_group_image1.jpg" alt="Snack Time"></img>
                        <div className="px-6 py-4">
                            <div className="font-bold text-xl mb-2">Who says no snacking between meals?</div>

                        </div>
                        <div className="px-6 py-4">
                            <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">#snacktime</span>
                            <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">#summerofsnacks</span>
                            <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">#fullstacksnacks</span>
                        </div>
                    </div>

                </section>

                <section className="flex-1">
                    <ul>
                        {this.state.snacks.map(snack => <SnackItem key={snack.id} snack={snack} />)}
                    </ul>
                    <SnackForm onSnackCreate={this.snackCreateHandler} />
                </section>
                </div>

                <style jsx>{`
            .container {
                text-align: center;
            }

        `}
                </style>

                <style jsx global>{`
                html,
                body {
                padding: 0;
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
                    Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue,
                    sans-serif;
                }

                * {
                box-sizing: border-box;
                }
            `}</style>

            <Footer />

            </div>
        )
    }
}

export default Home

// export async function getStaticProps() {
export async function getServerSideProps() {

    const response = await fetch(url);
    const snacks = await response.json();

    return {
        props: {
            snacks: snacks,
        },
    }
}
