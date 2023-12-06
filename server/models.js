const mongoose = require('mongoose');

const momoFamilySchema = new mongoose.Schema({
  ID: { type: Number, required: true },
  Name: { type: String, required: true },
  About: {
    role: [String],
    gender: String,
    birthdate: String,
    location: String
  },
  ProfilePic: String,
  CoverPhoto: String,
  Gallery: [String], // Assuming this is an array of image URLs
  Posts: [{ // Embedded document for posts
    PostID: String,
    Date: String,
    Caption: String,
    Media: {
      Url: String,
      Type: String
    }
  }],
  Bio: {
    Feature: String
  },
  Timeline: {
    Events: [{
      event_date: String,
      event_description: String
    }]
  }
});

const MomoFamily = mongoose.model('MomoFamily', momoFamilySchema);

module.exports = MomoFamily;