import React from 'react'

import { BrowserRouter as Router, Switch, Route } from "react-router-dom"

import Container from '@material-ui/core/Container'
import Typography from '@material-ui/core/Typography'

import './App.css'
import Frontpage from './components/Frontpage'
import CalendarView from './components/CalendarView'
import CalendarDetail from './components/CalendarDetail'
import CalendarEdit from './components/CalendarEdit'


function App() {
  return (
    <Router>
      <div className="app">
        <Container className="App" maxWidth="md">
          <Typography variant="h1" component="h1" gutterBottom align="center">
            Readyupper
          </Typography>

          <Switch>
            <Route path="/:calendarId/edit/">
              <CalendarView Child={CalendarEdit} />
            </Route>
            <Route path="/:calendarId">
              <CalendarView Child={CalendarDetail} />
            </Route>
            <Route path="/">
              <Frontpage />
            </Route>
          </Switch>
        </Container>
      </div>
    </Router>
  )
}

export default App
