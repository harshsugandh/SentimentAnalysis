import React, { Component } from 'react'
import {Form} from 'react-bootstrap'

export class BlankPage extends Component {


  render() {
    return (
      <div className="card">
               <div className="card-body">
                <h4 className="card-title">YouTube Comment Sentiment Analysis</h4>
                <form className="forms-sample">
                  <Form.Group className="row">
                    <label htmlFor="exampleInputUsername2" className="col-sm-3 col-form-label">Video ID</label>
                    <div className="col-sm-9">
                    <Form.Control type="text" className="form-control" id="exampleInputUsername2" placeholder="Video Id" />
                    </div>
                  </Form.Group>
                  <Form.Group className="row">
                    <label htmlFor="exampleInputEmail2" className="col-sm-3 col-form-label">Number of Comments</label>
                    <div className="col-sm-9">
                    <Form.Control type="email" className="form-control" id="exampleInputEmail2" placeholder="Number of Comments" />
                    </div>
                  </Form.Group>
                  {/*<Form.Group className="row">
                    <label htmlFor="exampleInputMobile" className="col-sm-3 col-form-label">Mobile</label>
                    <div className="col-sm-9">
                    <Form.Control type="text" className="form-control" id="exampleInputMobile" placeholder="Mobile number" />
                    </div>
                  </Form.Group>
                  <Form.Group className="row">
                    <label htmlFor="exampleInputPassword2" className="col-sm-3 col-form-label">Password</label>
                    <div className="col-sm-9">
                    <Form.Control type="password" className="form-control" id="exampleInputPassword2" placeholder="Password" />
                    </div>
                  </Form.Group>
                  <Form.Group className="row">
                    <label htmlFor="exampleInputConfirmPassword2" className="col-sm-3 col-form-label">Re Password</label>
                    <div className="col-sm-9">
                    <Form.Control type="password" className="form-control" id="exampleInputConfirmPassword2" placeholder="Password" />
                    </div>
                  </Form.Group>
                  <div className="form-check">
                    <label className="form-check-label text-muted">
                      <input type="checkbox" className="form-check-input"/>
                      <i className="input-helper"></i>
                      Remember me
                    </label>
                  </div>*/}
                  <button type="reset" className="btn btn-secondary mr-2">Reset</button>
                  <button type="submit" className="btn btn-primary mr-2" onClick="">Submit</button>
                  
                </form>
              </div> 
            </div>
    )
  }
}

export default BlankPage
