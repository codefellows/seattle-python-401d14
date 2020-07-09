import React from 'react'

export default class SnackForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            name : '',
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {

        const newName = event.target.value;
        this.setState({
            name: newName,
        })

    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.onSnackCreate(this.state);
        this.setState({name:''});
    }

    render() {
        return (


            <form onSubmit={this.handleSubmit} className="w-full max-w-sm">
            <div className="flex items-center border-b border-b-2 border-teal-500 py-2">
                <input name="snack-name" value={this.state.name} onChange={this.handleChange}
                className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Something yummy" aria-label="Snack"></input>
                <button className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded" type="submit">
                Enter Snack
                </button>
            </div>
            </form>
        )
    }
}
