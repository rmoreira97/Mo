import React, { useRef, Suspense, useState } from 'react';
import { Canvas, useFrame, useLoader } from 'react-three-fiber';
import { TextureLoader, DoubleSide } from 'three';
import { useNavigate } from 'react-router-dom';
import '../css/GorillaSelection.css';

function GorillaSelection() {
  const navigate = useNavigate();
  const [isBackButtonVisible, setIsBackButtonVisible] = useState(false);
  const gorillaImages = [
    { url: '/Assets/images/GorillaSelection/Momotaro.png', id: 2 },
    { url: '/Assets/images/GorillaSelection/Genki.png', id: 1 },
    { url: '/Assets/images/GorillaSelection/Gentaro.png', id: 3 },
    { url: '/Assets/images/GorillaSelection/Kintaro.png', id: 4 }
  ];

  // Handler for the wheel event
  const handleWheel = (event) => {
    if (event.deltaY > 0) {
      setIsBackButtonVisible(true);
    } else if (event.deltaY < 0 && window.scrollY === 0) {
      setIsBackButtonVisible(false);
    }
  };

  // Function to navigate to the correct route
  const navigateToAPIEndpoint = (gorillaId) => {
    navigate(`/gorillas/${gorillaId}`); // Use the correct route here
  };

  return (
    <div className="gorilla-container text-center py-5" onWheel={handleWheel}>
      <Canvas camera={{ position: [2, 0, 1.99] }}>
        <ambientLight intensity={0.5} />
        <directionalLight intensity={0.8} position={[2, 2, 2]} />
        <Suspense fallback={null}>
          {gorillaImages.map((gorilla, index) => (
            <GorillaImage
              key={index}
              image={gorilla.url}
              position={[-2 + index * 1.0, 0, 0]}
              onClick={() => navigateToAPIEndpoint(gorilla.id)}
            />
          ))}
        </Suspense>
      </Canvas>
      <button
        className="back-button"
        style={{ opacity: isBackButtonVisible ? 1 : 0, transition: 'opacity 0.5s' }}
        onClick={() => navigate('/')}
      >
        Back
      </button>
    </div>
  );
}

function GorillaImage({ image, position, onClick }) {
  const meshRef = useRef();
  const [isHovered, setIsHovered] = useState(false);
  const texture = useLoader(TextureLoader, image);

  useFrame(() => {
    if (!isHovered) {
      meshRef.current.rotation.y += 0.003;
    }
  });

  return (
    <mesh
      position={position}
      ref={meshRef}
      onClick={onClick}
      onPointerOver={() => setIsHovered(true)}
      onPointerOut={() => setIsHovered(false)}
    >
      <planeGeometry args={[1, 1]} />
      <meshBasicMaterial map={texture} transparent={true} side={DoubleSide} />
    </mesh>
  );
}

export default GorillaSelection;