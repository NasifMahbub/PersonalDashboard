import React, { Component } from 'react';
import './layout/home.css';
import axios from 'axios';

class Edit extends Component {

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/users/api/v1/2/')
      .then(res => {
        const data = res.data;
        console.log(data);
      });
      
  }

  render() {
    return (
      <div className="Edit">
        <div className="Edit-body">
          <h1>Welcome</h1>
          <p>This is the personal dashboard of {this.props.username} </p>
          <p>Name: {this.props.first_name}  {this.props.last_name}</p>
          <p>Email: {this.props.email}</p>
          <p>Contact No: {this.props.contact_no}</p>

          <img src={this.props.image} alt="" />
          <p></p>
        </div>
      </div>
    );
  }
}

export default Edit;