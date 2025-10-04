// GMap.jsx
import React, { useCallback, useRef } from 'react';
import { GoogleMap, Marker, useLoadScript } from '@react-google-maps/api';

const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

const containerStyle = {
    width: '100%',
    height: '100%',
};

const center = {
    lat: 47.760353,
    lng: -122.202102,
};

// fake location info
const restaurants = [
    { id: 1, name: 'Sushi Place', position: { lat: 47.761, lng: -122.202 } },
    { id: 2, name: 'Burger Town', position: { lat: 47.759, lng: -122.204 } },
    { id: 3, name: 'Taco Heaven', position: { lat: 47.758, lng: -122.200 } },
];

const GMap = () => {
    const { isLoaded, loadError } = useLoadScript({
        googleMapsApiKey: apiKey,
    });

    const mapRef = useRef();

    const onMapLoad = useCallback((map) => {
        mapRef.current = map;
    }, []);

    if (loadError) return <div>Error loading map</div>;
    if (!isLoaded) return <div>Loading Map...</div>;

    return (
        <div className="w-full h-full rounded-lg overflow-hidden">
            <GoogleMap
                mapContainerStyle={containerStyle}
                center={center}
                zoom={14}
                onLoad={onMapLoad}
            >
                {restaurants.map((restaurant) => (
                    <Marker
                        key={restaurant.id}
                        position={restaurant.position}
                        title={restaurant.name}
                    />
                ))}
            </GoogleMap>
        </div>
    );
};

export default GMap;
