import Axios from 'axios'
import React, { Component } from 'react'
import axios from 'axios'
export class WordCloud extends Component {    

    constructor(props) {
        super(props)
    
        this.state = {
             image: require ('../../assets/images/image.jpg')
        }
    }
    

    onClickHandler = e => {
        e.preventDefault()
        axios.post('/wordcloud')
        .then(response => {
            console.log(response)
            this.setState({
                image: require ('../../assets/images/wordcloud.jpg')
            });
        })
        .catch(error => {
            console.log(error)
        })
      }
    

    render() {
        return (
            <div>
                <button onClick={this.onClickHandler}>Generate Wordcloud</button>
                <br/> 
                <br/>
                <img src={this.state.image} />
            </div>
            
        )
    }
}

export default WordCloud
