const URL_BASE =
  "https://todoapp-50614-default-rtdb.europe-west1.firebasedatabase.app";

export const FIREBASE_ENDPOINTS = {
  tasks: `${URL_BASE}/tasks2.json`,

  dettaglioTasks: (id) => `${URL_BASE}/tasks2/${id}.json`,
};
