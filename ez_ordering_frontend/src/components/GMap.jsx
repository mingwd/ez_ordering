// GMap.jsx
import React, { useCallback, useRef, useState } from 'react';
import { GoogleMap, useLoadScript } from '@react-google-maps/api';

const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

const mapContainerStyle = {
    width: '95%',
    height: '95%',
};

const center = {
    lat: 47.76035329082079, // Bothell
    lng: -122.20210234249339,
};

const GMap = () => {
    const { isLoaded, loadError } = useLoadScript({
        googleMapsApiKey: apiKey,
        libraries: ['places'],
    });

    const mapRef = useRef();
    const onMapLoad = useCallback((map) => {
        mapRef.current = map;
    }, []);

    if (loadError) return <div>Error loading maps</div>;
    if (!isLoaded) return <div>Loading Maps...</div>;

    return (
        <div className="w-full h-full rounded-lg overflow-hidden">
            <GoogleMap
                mapContainerStyle={mapContainerStyle}
                zoom={12}
                center={center}
                onLoad={onMapLoad}
            />
        </div>
    );
};

export default GMap;
