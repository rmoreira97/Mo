import React, { Suspense, useState, useEffect } from 'react';
import { Canvas, useLoader } from 'react-three-fiber';
import { OrbitControls, Text } from '@react-three/drei';
import { TextureLoader } from 'three';
import { useNavigate } from 'react-router-dom';
import '../css/LandingPage.css';

function LandingPageContent() {
  const navigate = useNavigate();
  const familyTexture = useLoader(TextureLoader, '/Assets/images/family.png');
  const [viewportWidth, setViewportWidth] = useState(window.innerWidth);

  useEffect(() => {
    function handleResize() {
      setViewportWidth(window.innerWidth);
    }

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  // Adjust scale and position based on viewport width
  const scale = viewportWidth < 431 ? [0.1, 0.1, 0.1] : [0.2, 0.2, 0.2];
  const textPosition = viewportWidth < 431 ? [0, 0.4, 0.6] : [0, 1, -1];
  const spritePosition = viewportWidth < 431 ? [0, 0.20, 1] : [0, 0.5, 0];
  const spriteScale = viewportWidth < 431 ? [0.5, 0.5, 0.5] : [1, 1, 1];

  return (
    <>
      <ambientLight intensity={0.2} />
      <Text 
        position={textPosition}
        scale={scale}
        rotation={[-0.3, 0, 0]}
      >
        The Momotaro Family
      </Text>
      <sprite position={spritePosition} scale={spriteScale}>
        <spriteMaterial attach="material" map={familyTexture} />
      </sprite>
      <Text
        position={[0, 0, 1.6]}
        scale={viewportWidth < 431 ? [0.05, 0.05, 0.05] : [0.1, 0.1, 0.1]}
        rotation={[-1, 0, 0]}
        onClick={() => navigate('/selection')}
      >
        Explore Now
      </Text>
      <OrbitControls />
    </>
  );
}

function LandingPage() {
  return (
    <div className="landing-container text-center py-5" style={{ height: '100vh', width: '100vw' }}>
      <Canvas camera={{ position: [0, 0, 2] }}>
        <Suspense fallback={null}>
          <LandingPageContent />
        </Suspense>
      </Canvas>
    </div>
  );
}

export default LandingPage;