const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const mongoose = require('mongoose');
const MomoFamily = require('./models');

dotenv.config({ path: __dirname + '/.env' });

const app = express();
app.use(cors());
app.use(express.json()); // To parse JSON bodies

const port = process.env.PORT || 3001;
const mongoUri = process.env.MONGO_URI;

mongoose.connect(mongoUri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => {
  console.log('MongoDB connected successfully');
  app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
})
.catch((err) => {
  console.error('MongoDB connection error:', err);
});

// Get all gorillas
app.get('/api/gorillas', async (req, res) => {
  try {
    const gorillas = await MomoFamily.find();
    res.json({ gorillas });
  } catch (error) {
    res.status(500).send('Internal server error');
  }
});

/// Get a single gorilla by custom ID
app.get('/api/gorillas/:id', async (req, res) => {
    try {
      const gorilla = await MomoFamily.findOne({ ID: req.params.id });
      if (gorilla) {
        res.json({ gorilla });
      } else {
        res.status(404).send('Gorilla not found');
      }
    } catch (error) {
      res.status(500).send('Internal server error');
    }
  });
  
  // Get gorilla posts by custom ID
  app.get('/api/gorillas/:id/posts', async (req, res) => {
    try {
      const gorilla = await MomoFamily.findOne({ ID: req.params.id });
      if (gorilla) {
        res.json({ posts: gorilla.Posts });
      } else {
        res.status(404).send('Gorilla not found');
      }
    } catch (error) {
      res.status(500).send('Internal server error');
    }
  });
  
  // Add a post to a gorilla by custom ID
  app.post('/api/gorillas/:id/addPost', async (req, res) => {
    try {
      const gorilla = await MomoFamily.findOne({ ID: req.params.id });
      if (gorilla) {
        const newPost = req.body;
        gorilla.Posts.push(newPost);
        await gorilla.save();
        res.status(201).json({ newPost });
      } else {
        res.status(404).send('Gorilla not found');
      }
    } catch (error) {
      res.status(500).send('Internal server error');
    }
  });
  
  // Update a gorilla by custom ID
  app.put('/api/gorillas/:id', async (req, res) => {
    try {
      const gorilla = await MomoFamily.findOneAndUpdate(
        { ID: req.params.id },
        req.body,
        { new: true }
      );
      if (gorilla) {
        res.json({ gorilla });
      } else {
        res.status(404).send('Gorilla not found');
      }
    } catch (error) {
      res.status(500).send('Internal server error');
    }
  });

// ... (Other routes as needed)

module.exports = app;
