import { initializeApp } from "firebase/app";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: "AIzaSyD93bzTpcbL8cYjrwyMTdh0zZJSsKcioZ4",
  authDomain: "mofamily-4c06a.firebaseapp.com",
  projectId:"mofamily-4c06a",
  storageBucket: "mofamily-4c06a.appspot.com",
  messagingSenderId: "136591470992",
  appId: "1:136591470992:web:d5c3650aceb0b762984315",
  measurementId: "G-FFDQQR24R0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase Storage
const storage = getStorage(app);


console.log( firebaseConfig.storageBucket);
export default storage;
