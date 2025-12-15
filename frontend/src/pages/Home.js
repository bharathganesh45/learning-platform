import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import './Home.css';

const Home = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="home">
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <h1 className="hero-title">Learn Anything, Anytime, Anywhere</h1>
            <p className="hero-subtitle">
              Discover thousands of courses from expert instructors and advance your career
            </p>
            <div className="hero-actions">
              {isAuthenticated ? (
                <Link to="/dashboard" className="btn btn-primary btn-large">
                  Go to Dashboard
                </Link>
              ) : (
                <>
                  <Link to="/register" className="btn btn-primary btn-large">
                    Get Started
                  </Link>
                  <Link to="/courses" className="btn btn-outline btn-large">
                    Browse Courses
                  </Link>
                </>
              )}
            </div>
          </div>
        </div>
      </section>

      <section className="features">
        <div className="container">
          <h2 className="section-title">Why Choose Us?</h2>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">📚</div>
              <h3>Wide Range of Courses</h3>
              <p>Access thousands of courses across various subjects and skill levels</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">👨‍🏫</div>
              <h3>Expert Instructors</h3>
              <p>Learn from industry professionals and experienced educators</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">📈</div>
              <h3>Track Your Progress</h3>
              <p>Monitor your learning journey and see your improvement over time</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🎯</div>
              <h3>Flexible Learning</h3>
              <p>Learn at your own pace, whenever and wherever you want</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;

