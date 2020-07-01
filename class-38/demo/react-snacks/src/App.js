import React from 'react';
import './App.css';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            snacks : [
                {
                    id: 1,
                    name: 'apple',
                    type: 'fruit',
                },
                {
                    id: 2,
                    name: 'snickers',
                    type: 'candy',
                }

            ],
            popularSnack: '???'
        }

        this.snackCreatedHandler = this.snackCreatedHandler.bind(this);
    }

    snackCreatedHandler(snack) {
        alert(snack.name);
        const updatedSnacks = this.state.snacks;
        updatedSnacks.push({name:"???",type:"???",id:"???"})
        this.setState({
            snacks : updatedSnacks
        })
    }

    render() {
        return (
        <div className="App">
            <Header popularSnack={this.state.popularSnack} />
            <main>
                <SnackList snacks={this.state.snacks} onSnackCreate={this.snackCreatedHandler} />
            </main>
            <Footer text="whatever" />
        </div>
        )
    }

}

function SnackList(props) {

    // need a function to call when creating a new thing
    // function should be in props

    return (
        <>
        <h2>Snacks</h2>
        <ul>
           {props.snacks.map(snack => <Snack item={snack} key={snack.id} />)}
        </ul>
        <SnackForm onSnackCreate={props.onSnackCreate} />
        </>

    )
}

class SnackForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            name : '???',
            snackType: '',
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        const newName = event.target.value;
        this.setState({
            name: newName
        })
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.onSnackCreate(this.state);
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Name:
                    <input
                    type="text" value={this.state.name} onChange={this.handleChange}>
                    </input>
                </label>
            </form>
        )
    }
}

function Snack(props) {
    return <li>I am snack {props.item.name}</li>
}


function Header(props) {

    return <h2>Popular snack is {props.popularSnack}</h2>
}

function Footer(props) {
    return <footer><small>{props.text}</small></footer>
}

export default App;
