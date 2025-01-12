import React from 'react';
import Products from './components/Products'; // Adjust path if needed

function App() {
    return (
        <div>
            <header style={{ textAlign: 'center', padding: '1rem', background: '#f4f4f4' }}>
                <h1>فروشگاه آنلاین نقاشی</h1>
            </header>
            <main style={{ padding: '1rem' }}>
                <Products />
            </main>
        </div>
    );
}

export default App;
