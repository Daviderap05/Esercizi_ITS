import { StyleSheet } from 'react-native'
import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack'

import Home from './src/es6/es6_3/src/screen/home/Home'
import AddTask from './src/es6/es6_3/src/screen/AddTask'
import ToDo from './src/es6/es6_3/src/screen/ToDo'
import Finished from './src/es6/es6_3/src/screen/Finished'

const App = () => {

  const Stack = createNativeStackNavigator()

  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={Home} />

        <Stack.Screen name="Add" component={AddTask} />

        <Stack.Screen name="ToDo" component={ToDo} />

        <Stack.Screen name="Finished" component={Finished} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App

const styles = StyleSheet.create({})