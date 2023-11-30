// GorillaProfile.js
import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Link, useParams } from 'react-router-dom';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../css/GorillaProfile.css';
// import { ref, uploadBytes, getDownloadURL } from 'firebase/storage';
// import { storage } from '../firebaseConfig'; // Adjust the import path as necessary
import { Post } from './Post'; // for named import // Assuming that both GorillaProfile.jsx and Post.jsx are in the same directory


// SVG Icons
const GenderIcon = '/Assets/images/person.svg';
const BirthdayIcon = '/Assets/images/birthday.svg';
const LocationIcon = '/Assets/images/location.svg';

function GorillaProfile() {
  const { id } = useParams();
  const [gorilla, setGorilla] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [editedGallery, setEditedGallery] = useState([]);
  const [newGalleryUrl, setNewGalleryUrl] = useState('');
  const isAdmin = true; // Replace with actual admin check
  const [isDragging, setIsDragging] = useState(false);
  const [initialPosition, setInitialPosition] = useState({ x: 0, y: 0 });
  const galleryRef = useRef(null);
  const [activeTab, setActiveTab] = useState('profile')
  const timelineRef = useRef(null);
  // const [posts, setPosts] = useState([]);
  // const [caption, setCaption] = useState('');
  // const [file, setFile] = useState(null);





 


  function FadeInSection(props) {
    const [isVisible, setVisible] = useState(false);
    const domRef = useRef();
  
    useEffect(() => {
      const observer = new IntersectionObserver(entries => {
        // Only change the state if the new value is different
        // and only for the first entry (assuming one element is observed)
        if (entries[0].isIntersecting !== isVisible) {
          setVisible(entries[0].isIntersecting);
        }
      });
  
      const currentElement = domRef.current;
  
      if (currentElement) {
        observer.observe(currentElement);
      }
  
      return () => {
        // Cleanup the observer if the component is unmounted or the ref changes
        if (currentElement) {
          observer.unobserve(currentElement);
        }
      };
    }, [isVisible]); // Only re-run the effect if isVisible changes
  
    return (
      <div
        className={`fade-in-section ${isVisible ? 'is-visible' : ''}`}
        ref={domRef}
      >
        {props.children}
      </div>
    );
  }
  
  
  useEffect(() => {
    const gorillaId = parseInt(id, 10);
    if (isNaN(gorillaId)) {
      setError('Invalid Gorilla ID.');
      setLoading(false);
      return;
    }

    fetch(`http://127.0.0.1:5000/api/gorillas/${gorillaId}`)
      .then(response => response.json())
      .then(data => {
        console.log('Received data:', data); // Log the data object
        setGorilla(data);
        setEditedGallery(data.Gallery || []);
        setLoading(false);
      })
      .catch(error => {
        setError(error.message);
        setLoading(false);
      });
  }, [id]);


  
  const openEditor = () => {
    setIsEditing(true);
    
    setEditedGallery(gorilla.Gallery);
  };
  const closeEditor = () => setIsEditing(false);

  
  const handleNewGalleryUrlChange = (e) => setNewGalleryUrl(e.target.value);

  const handleAddGalleryUrl = () => {
    if (newGalleryUrl.trim() !== '') {
      setEditedGallery([...editedGallery, newGalleryUrl]);
      setNewGalleryUrl('');
    }
  };

  const saveChanges = () => {
    // Assuming your backend expects an object with Bio and Gallery properties
    const updatedGorilla = {
      ...gorilla,
      Gallery: editedGallery,
    };

    fetch(`http://127.0.0.1:5000/api/gorillas/${gorilla.ID}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updatedGorilla),
    })
      .then(response => response.json())
      .then(data => {
        setGorilla(data);
        setIsEditing(false);
      })
      .catch(error => {
        setError('Error updating gorilla');
        console.error('Error updating gorilla:', error);
      });
  };

  

  const handleTabClick = (tab) => {
    setActiveTab(tab);
  };

  const renderContent = () => {
    switch (activeTab) {
      case 'profile':
        return (
          <>
            <div className="bio-section">
              {gorilla.Bio && gorilla.Bio.Feature && <p>{gorilla.Bio.Feature}</p>}
            </div>
  
            <div className="gallery-preview"
                 ref={galleryRef}
                 onMouseDown={handleMouseDown}
                 onMouseUp={handleMouseUp}
                 onMouseMove={handleMouseMove}
                 onMouseLeave={handleMouseLeave}>
              {gorilla.Gallery.slice(0, 3).map((imageUrl, index) => (
                <img key={index}
                     src={imageUrl}
                     alt={`Gallery item ${index}`}
                     className="img-fluid gallery-item" />
              ))}
            </div>
  
            <div className="timeline" ref={timelineRef}>
              {gorilla.Timeline && Array.isArray(gorilla.Timeline.Events) &&
                gorilla.Timeline.Events.map((event, index) => (
                  <FadeInSection key={index}>
                    <div className={`container ${index % 2 === 0 ? 'left' : 'right'}`}>
                      <div className="content">
                        <h2>{event.event_date}</h2>
                        <p>{event.event_description}</p>
                      </div>
                    </div>
                  </FadeInSection>
                ))}
            </div>
          </>
        );
      case 'gallery':
        return (
          <div className="gallery-container"
               ref={galleryRef}
               onMouseDown={handleMouseDown}
               onMouseUp={handleMouseUp}
               onMouseMove={handleMouseMove}
               onMouseLeave={handleMouseLeave}>
            {gorilla.Gallery.map((imageUrl, index) => (
              <img key={index}
                   src={imageUrl}
                   alt={`Gallery item ${index}`}
                   className="img-fluid" />
            ))}
          </div>
        );
      case 'videos':
        return (
          <div className="video-section">
            <p>Videos coming soon...</p>
          </div>
        );
      
        
        case 'posts':
  return (
    <Post gorillaId={id} />
  );
default:
  return null;
  }
};



  
  // Drag handlers for the gallery
  const handleMouseDown = (e) => {
    e.preventDefault();
    setIsDragging(true);
    setInitialPosition({ x: e.clientX, y: e.clientY });
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  const handleMouseMove = (e) => {
    if (isDragging && galleryRef.current) {
      const dx = initialPosition.x - e.clientX;
      galleryRef.current.scrollLeft += dx;
      setInitialPosition({ x: e.clientX, y: e.clientY });
    }
  };

  const handleMouseLeave = () => {
    setIsDragging(false);
  };

  const renderAboutSection = () => {
    if (!gorilla || !gorilla.About) {
      return null;
    }
  
    return (
      <div className="about-section">
        <div className="about-name">
          {gorilla.Name} {/* Dynamically insert the name */}
        </div>
        <div className="about-role">
          {gorilla.About.role.join(', ')} {/* Join roles with a comma */}
        </div>
        <div className="about-item about-item-gender">
  <img src={GenderIcon} alt="Gender" className="about-icon" />
  <span className="about-text">{gorilla.About.gender}</span>
</div>
<div className="about-item about-item-birthday">
  <img src={BirthdayIcon} alt="Birthdate" className="about-icon" />
  <span className="about-text">{`${gorilla.About.birthdate}`}</span>
</div>
<div className="about-item about-item-location">
  <img src={LocationIcon} alt="Location" className="about-icon" />
  <span className="about-text">{gorilla.About.location}</span>
</div>
      </div>
    );
  };
  
  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!gorilla) {
    return <div>Gorilla not found.</div>;
  }

  return (
    <div className="profile-container">
      <div className="row">
        <div className="col-md-4">
          <img
            src={gorilla.ProfilePic}
            alt={gorilla.name}
            className="profile-image"
          />
        </div>
        <div className="cover-photo-container"> 
        <img src={gorilla.CoverPhoto}  alt="Cover" className="cover-photo"/>
        </div>
        <div className="col-md-8">
          {renderAboutSection()}
        </div>
      </div>
    
        <div className="tabs">
  <button onClick={() => handleTabClick('profile')} className={`btn btn-outline-primary ${activeTab === 'profile' ? 'active-tab' : ''}`}>Profile</button>
  <button onClick={() => handleTabClick('gallery')} className={`btn btn-outline-primary ${activeTab === 'gallery' ? 'active-tab' : ''}`}>Gallery</button>
  <button onClick={() => handleTabClick('posts')} className={`btn btn-outline-primary ${activeTab === 'posts' ? 'active-tab' : ''}`}>Posts</button>
  <button onClick={() => handleTabClick('videos')} className={`btn btn-outline-primary ${activeTab === 'videos' ? 'active-tab' : ''}`}>Videos</button>
</div>
    
{renderContent()}

{isAdmin && (
  <Button variant="primary" onClick={openEditor} className="edit-profile-btn">
    Edit Profile
  </Button>
)}

<Modal show={isEditing} onHide={closeEditor} size="lg">
  <Modal.Header closeButton>
    <Modal.Title>Gallery Editor</Modal.Title>
  </Modal.Header>
  <Modal.Body>
    <Form>
    
      
      <Form.Group controlId="formGallery">
        <Form.Label>Gallery URLs</Form.Label>
        {editedGallery.map((url, index) => (
          <div key={index} className="d-flex align-items-center mb-2">
            <Form.Control
              type="text"
              value={url}
              readOnly
              className="me-2"
            />
            <Button variant="danger" onClick={() => {
              setEditedGallery(editedGallery.filter((_, i) => i !== index));
            }}>
              Remove
            </Button>
          </div>
        ))}
        <div className="d-flex align-items-center">
          <Form.Control
            type="text"
            value={newGalleryUrl}
            onChange={handleNewGalleryUrlChange}
            placeholder="Enter new image URL"
            className="me-2"
          />
          <Button variant="success" onClick={handleAddGalleryUrl}>
            Add
          </Button>
        </div>
      </Form.Group>
      {/* Buttons inside the form at the end of the modal body */}
      <div className="modal-footer-buttons">
    <Button variant="secondary" onClick={closeEditor} className="btn-close me-2">
     
    </Button>
    <Button variant="primary" onClick={saveChanges} className="btn-save">
      Save Changes
    </Button>
      </div>
    </Form>
  </Modal.Body>
</Modal>
  
      <div className="back-button-container">
        <Link to="/selection" className="btn btn-primary">
          Back
        </Link>
      </div>
    </div>
  );
}

                export default GorillaProfile;
