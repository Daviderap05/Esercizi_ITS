const BASE_URL =
  "https://todoapp-50614-default-rtdb.europe-west1.firebasedatabase.app";

export const FIREBASE_ENDPOINTS = {
  tasks: `${BASE_URL}/tasks3.json`,
  dettaglioTasks: (id) => `${BASE_URL}/tasks3/${id}.json`,
};
