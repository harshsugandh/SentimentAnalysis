import React, { Component } from 'react'




function RenderTableData({posts}) {
    console.log(posts)
    console.log("dsijsiudhuiw")


   if(posts.length == 0){
       return (
           <div>
           </div>
       )
   }
    return(
      <table id='posts' className="table">
        <thead>
            <tr>
              <th>S No.</th>
              <th>Comments</th>
              <th>Sentiment Score</th>
            </tr>
        </thead>
        <tbody>
          {
          posts.map((post, index) => {
          const {comment, sentiment} = post //destructuring
          return (

            <tr key={index}>
              <td>{index+1}</td>
              <td>{comment}</td>
              <td>{sentiment}</td>
            </tr>
            )}
          )}
        </tbody>
      </table>
      )}


class Result extends Component {

    constructor(props) {
        super(props)
    
        this.state = {
             
        }
    }
    
    render() {
        //const posts = this.props.posts
        const posts = this.props.location.state.detail
        console.log(this.props.location.state.detail)
        //console.log("this is suupoosed to be ",this.props.posts)
        const data = <RenderTableData  posts = {posts}/>
        return (
            <div>
                {data}
            </div>
        )
    }
}

export default Result
