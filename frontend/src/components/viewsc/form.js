import React, { Component } from 'react';
import { connect } from 'react-redux';
import { createContainer, getSchedules } from '../../actions/containers';
import { PropTypes } from 'prop-types';

class Form extends Component {
  state = {
        name: "",
        schedule: {},
        size: "",
        weight: ""
    };

    static propTypes = {
      createContainer: PropTypes.func.isRequired,
      getSchedules: PropTypes.func.isRequired,
    };

  componentDidMount() {
      this.props.getSchedules();
  }

  handleSubmit = (e) => {
      e.preventDefault();

      const { name, schedule, size, weight } = this.state;

      const container = {
          name,
          schedule,
          size,
          weight
      };

    this.props.createContainer(container);

    // Reset the form
      this.setState({
        name: "",
        schedule: {},
        size: "",
        weight: ""
      });
  };

  render() {
      const { name, schedule, size, weight } = this.state;
      const { schedules } = this.props;

    return (
      <form onSubmit={this.handleSubmit}>
        <input
          type="text"
          placeholder="Название"
          value={name}
          onChange={(e) => this.setState({ name: e.target.value })}
        />
        <select
          value={schedule}
          onChange={(e) => this.setState({ schedule: e.target.value })}
        >
          <option value=''>Выберите форму</option>
          {schedules && schedules.length > 0 ? (
            schedules.map((schedule) => (
              <option key={schedule.id} value={schedule}>
                {schedule.name}
              </option>
            ))
          ) : (
            <option value='' disabled>
              Загрузка...
            </option>
          )}
        </select>
        <input
          type="text"
          placeholder="Размеры контейнера"
          value={size}
          onChange={(e) => this.setState({ size: e.target.value })}
        />
        <input
          type="text"
          placeholder="Weight"
          value={weight}
          onChange={(e) => this.setState({ weight: e.target.value })}
        />
        <button type="submit">Create Container</button>
      </form>
    );
  }
}

const mapStateToProps = (state) => ({
  schedules: state.schedules.schedules
});
export default connect(mapStateToProps, { createContainer, getSchedules })(Form);