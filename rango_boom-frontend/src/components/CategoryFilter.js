import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './CategoryFilter.css'; // Add CSS for styling

const CategoryFilter = ({ onCategorySelect }) => {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        axios
            .get('http://127.0.0.1:8000/api/categories/')
            .then((response) => {
                setCategories(response.data);
            })
            .catch((error) => {
                console.error('Error fetching categories:', error);
            });
    }, []);

    const renderCategoryTree = (categories) => {
        return categories.map((category) => (
            <li key={category.id}>
                <div
                    onClick={() => onCategorySelect(category.id)}
                    className="category-item"
                >
                    {category.icon && (
                        <img
                            src={category.icon}
                            alt={category.name}
                            className="category-icon"
                            style={{ width: '20px', marginRight: '8px' }}
                        />
                    )}
                    {category.name}
                </div>
                {category.children && category.children.length > 0 && (
                    <ul className="subcategory-list">
                        {renderCategoryTree(category.children)}
                    </ul>
                )}
            </li>
        ));
    };

    return (
        <div className="category-filter">
            <h3>دسته‌بندی:</h3>
            <ul className="category-list">
                {renderCategoryTree(categories)}
            </ul>
        </div>
    );
};

export default CategoryFilter;
