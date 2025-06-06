import React from 'react';
import GMap from '../components/gmap';

const OrderPage = () => {
    return (
        <div className="flex w-[90vw] h-[90vh] mx-auto bg-gray-50 p-4">
            <div className="flex flex-1">
                <div className="w-2/3 border-r">
                    <GMap />
                </div>
                <div className="w-1/3">Restaurant List</div>
            </div>
        </div>
    );
};

export default OrderPage;
