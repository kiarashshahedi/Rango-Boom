import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CategoryFilter from './CategoryFilter';

const Products = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [selectedCategory, setSelectedCategory] = useState(null);

    const fetchProducts = (category = null) => {
        setLoading(true);
        let url = 'http://127.0.0.1:8000/api/products/';
        if (category) {
            url += `?category=${category}`;
        }
        axios
            .get(url)
            .then((response) => {
                setProducts(response.data);
                setLoading(false);
            })
            .catch((error) => {
                console.error('Error fetching products:', error);
                setLoading(false);
            });
    };

    useEffect(() => {
        fetchProducts(selectedCategory);
    }, [selectedCategory]);

    const handleCategorySelect = (categoryId) => {
        setSelectedCategory(categoryId);
    };

    if (loading) return <p>در حال بارگذاری...</p>;

    return (
        <div>
            <h1>محصولات</h1>
            <CategoryFilter onCategorySelect={handleCategorySelect} />
            <div className="product-list">
                {products.length > 0 ? (
                    products.map((product) => (
                        <div key={product.id} className="product-card">
                            {product.image && (
                                <img
                                    src={product.image}
                                    alt={product.name}
                                    className=""
                                    style={{ width: '150px', height: '150px', marginRight: '100px' }}
                                />
                            )}
                            <h2>{product.name}</h2>
                            <p>{product.description}</p>
                            <p>
                                <strong>قیمت:</strong> {product.price} تومان
                            </p>
                            <p>
                                <strong>دسته‌بندی:</strong> {product.category.name}
                            </p>
                        </div>
                    ))
                ) : (
                    <p>هیچ محصولی یافت نشد.</p>
                )}
            </div>
        </div>
    );
};

export default Products;
