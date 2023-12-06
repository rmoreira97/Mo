import React, { useState, useEffect, useCallback } from 'react';
import { ref, uploadBytes, getDownloadURL } from 'firebase/storage';
import storage from '../firebaseConfig';
import '../css/Post.css';

function Post({ gorillaId }) {
  const [caption, setCaption] = useState('');
  const [file, setFile] = useState(null);
  const [posts, setPosts] = useState([]);

  const fetchPosts = useCallback(async () => {
    console.log('Fetching posts for gorillaId:', gorillaId);
  
    try {
      const response = await fetch(`http://localhost:3001/api/gorillas/${gorillaId}/posts`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log('Fetched posts data:', data);
  
      // Check if data has a 'posts' property and it's an array
      if (data && data.posts && Array.isArray(data.posts)) {
        setPosts(data.posts);
      } else {
        console.error('Data does not contain posts:', data);
        setPosts([]);
      }
    } catch (error) {
      console.error('Error fetching posts:', error);
      setPosts([]);
    }
  }, [gorillaId]);

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
    if (!file) {
      console.error('No file selected for upload');
      return;
    }
    
    const isVideo = file.type.startsWith('video/');
    const storageRef = ref(storage, `posts/${gorillaId}/${file.name}`);

    uploadBytes(storageRef, file)
      .then(snapshot => getDownloadURL(snapshot.ref))
      .then(downloadURL => {
        const newPost = {
          Date: new Date().toISOString(),
          Caption: caption,
          Media: {
            Type: isVideo ? 'video' : 'image',
            Url: downloadURL,
          },
        };

        setPosts(prevPosts => [...prevPosts, newPost]);

        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newPost),
        };

        return fetch(`http://localhost:3001/api/gorillas/${gorillaId}/addPost`, requestOptions);
      })
      .then(response => {
        if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Post successfully saved to server', data);
      })
      .catch(error => {
        console.error('Error during the upload or saving process:', error);
      });
  };

  return (
    <div>
      <div className="posts-list">
        {posts.length > 0 ? posts.map((post, index) => (
          <div key={index} className="post-item">
            <p className='caption'>{post.Caption}</p>
            {post.Media && post.Media.Type === 'image' ? (
              <img src={post.Media.Url} alt="Post" className="post-image" />
            ) : (
              <video controls src={post.Media.Url} className="post-video" />
            )}
          </div>
        )) : (
          <p>No posts to display.</p>
        )}
      </div>
    </div>
  );
}

export { Post };
