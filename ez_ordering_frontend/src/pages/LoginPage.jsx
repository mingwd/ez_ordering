import React, { useState } from 'react';

const LoginPage = () => {
    const [formData, setFormData] = useState({ username: '', password: '' });
    const [error, setError] = useState('');

    const handleChange = e => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async e => {
        e.preventDefault();

        const res = await fetch('http://localhost:8000/django/customer/f-login/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify(formData),
        });

        const data = await res.json();

        if (data.success) {
            window.location.href = '/customer/order';
        } else {
            setError(data.error || 'Login failed');
        }
    };

    return (
        <div className="flex items-center justify-center h-screen bg-orange-300">
            <div className="w-full max-w-md p-8 bg-white shadow-lg rounded-lg">
                <h1 className="text-3xl font-bold text-center mb-6">🍽️ EZ Ordering</h1>

                <form className="space-y-4" onSubmit={handleSubmit}>
                    <div>
                        <label className="block text-sm font-medium mb-1">Username</label>
                        <input name="username" onChange={handleChange} className="w-full px-4 py-2 border rounded-md" />
                    </div>
                    <div>
                        <label className="block text-sm font-medium mb-1">Password</label>
                        <input type="password" name="password" onChange={handleChange} className="w-full px-4 py-2 border rounded-md" />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-[#f2f2f2] text-black py-2 rounded-md hover:bg-[#e0e0e0] transition-colors"
                        style={{ backgroundColor: '#f2f2f2', color: '#2f2f2f' }}
                    >
                        Log In
                    </button>
                </form>

                {error && <p className="text-red-500 text-sm mt-4 text-center">{error}</p>}
                <p className="text-sm text-gray-500 text-center mt-6 text-red-500">
                    Credentials provided in resume.
                </p>
            </div>
        </div>
    );
};

export default LoginPage;
