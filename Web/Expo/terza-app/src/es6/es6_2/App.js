import { StatusBar } from "expo-status-bar";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import HomeScreen from "./src/es6/es6_2/components/HomeScreen";
import AddTask from "./src/es6/es6_2/components/AddTask";
import ViewTasks from "./src/es6/es6_2/components/ViewTasks";
import EditTask from "./src/es6/es6_2/components/EditTask";
import ViewTasksCompletate from "./src/es6/es6_2/components/ViewTasksCompletate";

export default function App() {
  const Stack = createNativeStackNavigator();

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="HomeScreen">
        <Stack.Screen name="HomeScreen" component={HomeScreen} />

        <Stack.Screen name="AddTask" component={AddTask} />

        <Stack.Screen name="ViewTasks" component={ViewTasks} />

        <Stack.Screen name="EditTask" component={EditTask} />

        <Stack.Screen
          name="ViewTasksCompletate"
          component={ViewTasksCompletate}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}