const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const mongoose = require('mongoose');
const axios = require('axios');
const MomoFamily = require('./models/MomoFamily'); // Ensure this path is correct for your model
const MONGO_API_KEY = process.env.MONGO_API_KEY;

dotenv.config();

const app = express();

// Middleware setup
app.use(cors());
app.use(express.json()); // For parsing application/json

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useFindAndModify: false,
  useCreateIndex: true,
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Function to make MongoDB API call
async function fetchMongoDBData() {
  const data = JSON.stringify({
    "collection": "momofamilies",
    "database": "gorillas",
    "dataSource": "Cluster0",
    "projection": {
      "_id": 1
    }
  });

  const config = {
    method: 'all',
    url: 'https://us-east-1.aws.data.mongodb-api.com/app/data-qutas/endpoint/data/v1/action/findOne',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': MONGO_API_KEY, // Use the API key from the environment variable
    },
    data: data
  };

  try {
    const response = await axios(config);
    return response.data;
  } catch (error) {
    console.error(error);
    throw new Error('Failed to fetch data from MongoDB API');
  }
}


// get a single gorilla by ID
app.get('/api/gorillas/:gorilla_id', async (req, res) => {
    try {
      const gorilla = await MomoFamily.findById(req.params.gorilla_id);
      const mongoDBData = await fetchMongoDBData(); // Make the MongoDB API call
      if (gorilla) {
        res.json({ gorilla, mongoDBData });
      } else {
        res.status(404).send('Gorilla not found');
      }
    } catch (error) {
      res.status(500).send('Internal server error');
    }
  });
  
  // Get gorilla posts by gorilla ID
  app.get('/api/gorillas/:gorilla_id/posts', async (req, res) => {
    try {
      const gorilla = await MomoFamily.findById(req.params.gorilla_id);
      const mongoDBData = await fetchMongoDBData(); // Make the MongoDB API call
      if (gorilla) {
        res.json({ posts: gorilla.Posts, mongoDBData });
      } else {
        res.status(404).send('Gorilla not found');
      }
    } catch (error) {
      res.status(500).send('Internal server error');
    }
  });
  
  // Add a post to a gorilla by ID
  app.post('/api/gorillas/:gorilla_id/addPost', async (req, res) => {
    try {
      const gorilla = await MomoFamily.findById(req.params.gorilla_id);
      const mongoDBData = await fetchMongoDBData(); // Make the MongoDB API call
      if (gorilla) {
        const newPost = req.body;
        gorilla.Posts.push(newPost);
        await gorilla.save();
        res.status(201).json({ newPost, mongoDBData });
      } else {
        res.status(404).send('Gorilla not found');
      }
    } catch (error) {
      res.status(500).send('Internal server error');
    }
  });
  
  // Update a gorilla by ID
  app.put('/api/gorillas/:gorilla_id', async (req, res) => {
    try {
      const gorilla = await MomoFamily.findByIdAndUpdate(
        req.params.gorilla_id,
        req.body,
        { new: true } // Option to return the updated document
      );
      const mongoDBData = await fetchMongoDBData(); // Make the MongoDB API call
      if (gorilla) {
        res.json({ gorilla, mongoDBData });
      } else {
        res.status(404).send('Gorilla not found');
      }
    } catch (error) {
      res.status(500).send('Internal server error');
    }
  });
  
  // ... (Other routes as needed)
  
  // Server start
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });