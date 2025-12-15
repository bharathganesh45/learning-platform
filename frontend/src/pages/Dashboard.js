import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import api from '../services/api';
import './Dashboard.css';

const Dashboard = () => {
  const { user } = useAuth();
  const [enrollments, setEnrollments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchEnrollments();
  }, []);

  const fetchEnrollments = async () => {
    try {
      const response = await api.get('/enrollments/');
      setEnrollments(response.data.results || response.data);
    } catch (error) {
      console.error('Error fetching enrollments:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading dashboard...</div>;
  }

  return (
    <div className="dashboard">
      <div className="container">
        <div className="dashboard-header">
          <h1>Welcome back, {user?.username}!</h1>
          <p>Continue your learning journey</p>
        </div>

        {enrollments.length === 0 ? (
          <div className="empty-dashboard">
            <h2>You haven't enrolled in any courses yet</h2>
            <p>Browse our courses and start learning today!</p>
            <Link to="/courses" className="btn btn-primary btn-large">
              Browse Courses
            </Link>
          </div>
        ) : (
          <div className="enrollments-section">
            <h2>My Courses</h2>
            <div className="enrollments-grid">
              {enrollments.map((enrollment) => (
                <div key={enrollment.id} className="enrollment-card card">
                  {enrollment.course.thumbnail && (
                    <img
                      src={enrollment.course.thumbnail}
                      alt={enrollment.course.title}
                      className="card-img"
                    />
                  )}
                  <div className="card-body">
                    <div className="enrollment-header">
                      <h3 className="card-title">{enrollment.course.title}</h3>
                      <span className={`status-badge ${enrollment.is_completed ? 'completed' : 'in-progress'}`}>
                        {enrollment.is_completed ? 'Completed' : 'In Progress'}
                      </span>
                    </div>
                    <p className="card-text">
                      {enrollment.course.description.substring(0, 100)}...
                    </p>
                    <div className="progress-section">
                      <div className="progress-info">
                        <span>Progress: {enrollment.progress_percentage || 0}%</span>
                      </div>
                      <div className="progress-bar">
                        <div
                          className="progress-fill"
                          style={{ width: `${enrollment.progress_percentage || 0}%` }}
                        />
                      </div>
                    </div>
                    <Link
                      to={`/courses/${enrollment.course.id}`}
                      className="btn btn-primary btn-block"
                    >
                      {enrollment.is_completed ? 'Review Course' : 'Continue Learning'}
                    </Link>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Dashboard;

