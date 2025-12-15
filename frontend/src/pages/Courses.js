import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import './Courses.css';

const Courses = () => {
  const [courses, setCourses] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    category: '',
    level: '',
    search: '',
  });

  useEffect(() => {
    fetchCourses();
    fetchCategories();
  }, [filters]);

  const fetchCourses = async () => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      if (filters.category) params.append('category', filters.category);
      if (filters.level) params.append('level', filters.level);
      if (filters.search) params.append('search', filters.search);

      const response = await api.get(`/courses/?${params.toString()}`);
      setCourses(response.data.results || response.data);
    } catch (error) {
      console.error('Error fetching courses:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchCategories = async () => {
    try {
      const response = await api.get('/categories/');
      setCategories(response.data.results || response.data || []);
    } catch (error) {
      console.error('Error fetching categories:', error);
      setCategories([]);
    }
  };

  const handleFilterChange = (e) => {
    setFilters({
      ...filters,
      [e.target.name]: e.target.value,
    });
  };

  if (loading) {
    return <div className="loading">Loading courses...</div>;
  }

  return (
    <div className="courses-page">
      <div className="container">
        <h1 className="page-title">All Courses</h1>

        <div className="filters">
          <input
            type="text"
            name="search"
            placeholder="Search courses..."
            className="search-input"
            value={filters.search}
            onChange={handleFilterChange}
          />
          <select
            name="category"
            className="filter-select"
            value={filters.category}
            onChange={handleFilterChange}
          >
            <option value="">All Categories</option>
            {categories.map((cat) => (
              <option key={cat.id} value={cat.name}>
                {cat.name}
              </option>
            ))}
          </select>
          <select
            name="level"
            className="filter-select"
            value={filters.level}
            onChange={handleFilterChange}
          >
            <option value="">All Levels</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </div>

        {courses.length === 0 ? (
          <div className="no-courses">No courses found. Try adjusting your filters.</div>
        ) : (
          <div className="courses-grid">
            {courses.map((course) => (
              <div key={course.id} className="course-card card">
                {course.thumbnail && (
                  <img
                    src={course.thumbnail}
                    alt={course.title}
                    className="card-img"
                    onError={(e) => {
                      e.target.style.display = 'none';
                    }}
                  />
                )}
                <div className="card-body">
                  <div className="course-meta">
                    <span className="course-level">{course.level}</span>
                    <span className="course-price">
                      {course.is_free ? 'Free' : `$${course.price}`}
                    </span>
                  </div>
                  <h3 className="card-title">{course.title}</h3>
                  <p className="card-text">
                    {course.description && course.description.length > 120
                      ? `${course.description.substring(0, 120)}...`
                      : course.description || 'No description available'}
                  </p>
                  <div className="course-stats">
                    <span>📚 {course.lessons_count || 0} lessons</span>
                    <span>👥 {course.enrolled_count || 0} students</span>
                  </div>
                  <Link to={`/courses/${course.id}`} className="btn btn-primary btn-block">
                    View Course
                  </Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Courses;

