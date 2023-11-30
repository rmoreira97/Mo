
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
// import bootstrap css
import 'bootstrap/dist/css/bootstrap.min.css';
// Post.jsx
// import React, { useState, useEffect, useCallback } from 'react';
// import { ref, uploadBytes, getDownloadURL } from 'firebase/storage';
// import storage from  '../firebaseConfig'; // Adjusted the path

import React, { useState, useEffect, useCallback } from 'react';
import { ref, uploadBytes, getDownloadURL } from 'firebase/storage';
import storage from '../firebaseConfig';
import '../css/Post.css';

function Post({ gorillaId }) {
  const [caption, setCaption] = useState('');
  const [file, setFile] = useState(null);
  const [posts, setPosts] = useState([]);
  const id = gorillaId; // Use the gorillaId prop as the id

  const fetchPosts = useCallback(async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/gorillas/${id}/posts`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      // Check if data is an array
      if (Array.isArray(data)) {
        setPosts(data);
      } else {
        console.error('Data is not an array:', data);
        setPosts([]); // Set posts to an empty array if data is not an array
      }
    } catch (error) {
      console.error('Error fetching posts:', error);
      setPosts([]); // Set posts to an empty array in case of error
    }
  }, [id]);

  useEffect(() => {
    fetchPosts();
  }, [fetchPosts]);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleCaptionChange = (event) => {
    setCaption(event.target.value);
  };

  const uploadFile = () => {
    // Ensure a file is selected
    if (!file) {
      console.error('No file selected for upload');
      return;
    }
  
    // Determine if the file is a video based on its MIME type
    const isVideo = file.type.startsWith('video/');
    // Create a reference to the storage location
    const storageRef = ref(storage, `posts/${id}/${file.name}`);
  
    // Upload the file to Firebase Storage
    uploadBytes(storageRef, file)
      .then((snapshot) => {
        // After upload, get the download URL
        return getDownloadURL(snapshot.ref);
      })
      // After you get the download URL in the uploadFile function
.then(downloadURL => {
  const newPost = {
      Date: new Date().toISOString(),
      Caption: caption,
      Media: {
          Type: isVideo ? 'video' : 'image',
          Url: downloadURL,
      },
  };

  // Update the state with the new post
  setPosts(prevPosts => [...prevPosts, newPost]);

  // Send the new post object to your server
  const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newPost),
  };

  return fetch(`http://127.0.0.1:5000/api/gorillas/${id}/addPost`, requestOptions);
})
      .then(response => {
        // Check for a successful response from your server
        if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        return response.json();
      })
      .then(data => {
        // Log the response data from the server
        console.log('Post successfully saved to server', data);
      })
      .catch(error => {
        // Log any errors that occur during the upload or saving process
        console.error('Error during the upload or saving process:', error);
      });
  };

  return (
  <div>
    <div className="input-container">
      <input
        type="text"
        placeholder="What's on your mind?"
        value={caption}
        onChange={handleCaptionChange}
        className="text-input"
      />
      
      <input id="file-input" type="file" onChange={handleFileChange} accept="image/*,video/*" className="file-input" />
      <button onClick={uploadFile} className="upload-button">Upload</button>
    </div>
    <div className="posts-list">
      {posts.map((post, index) => (
        <div key={index} className="post-item">
          <p className='caption'>{post.Caption}</p>
          {post.Media && post.Media.Type === 'image' ? (
            <img src={post.Media.Url} alt="Post" className="post-image" />
          ) : (
            <video controls src={post.Media.Url} className="post-video" />
          )}
        </div>
      ))}
    </div>
  </div>
);
}

export { Post };
