import React, { Component, Fragment } from 'react'
import { connect } from 'react-redux';
import { PropTypes } from 'prop-types';
import { getContainers, delContainer ,toggleContainer} from '../../actions/containers';

class List extends Component {
  static propTypes = {
        containers: PropTypes.array.isRequired,
        delContainer: PropTypes.func.isRequired,
        toggleContainer: PropTypes.func.isRequired,
    };

    componentDidMount() {
        this.props.getContainers();
    }
    render() {
        return (
            <Fragment>
                <h2>Containers List</h2>
                    <ul className='containers_list'>
                        {this.props.containers.map(container => ( 
                            <li className='container' key={container.id}>
                                <h3>{container.name}</h3>
                                <p>{container.schedule.name}</p>
                                <p>{container.size}</p>
                                <p>{container.date}</p>
                                <div className='container__control'>
                                    <input className='container_done' onChange={this.props.toggleContainer.bind(this, container)} 
                                    type='checkbox'  defaultChecked={container.done}></input>
                                    <button 
                                        onClick={this.props.delContainer.bind(this, container.id)} 
                                        className='delete_btn'>Удалить</button>
                                </div>
                            </li>
                        ))}
                    </ul> 
          </Fragment>
        )
    }
}


const mapStateToProps = (state)=> ({ 
    containers: state.containers.containers || []
});

export default connect(mapStateToProps, {getContainers, delContainer, toggleContainer})(List);