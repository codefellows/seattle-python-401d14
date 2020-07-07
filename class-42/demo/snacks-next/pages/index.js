import React from 'react'
import axios from 'axios'
import Nav from '../components/Nav'
import SnackForm from '../components/SnackForm'
import SnackItem from '../components/SnackItem'

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
                <Nav />
                <h1>Snacks Home</h1>
                <ul>
                    {this.state.snacks.map(snack => <SnackItem key={snack.id} snack={snack} />)}
                </ul>
                <SnackForm onSnackCreate={this.snackCreateHandler} />

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
