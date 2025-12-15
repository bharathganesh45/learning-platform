import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import api from '../services/api';
import './CourseDetail.css';

const CourseDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();
  const [course, setCourse] = useState(null);
  const [enrollment, setEnrollment] = useState(null);
  const [loading, setLoading] = useState(true);
  const [enrolling, setEnrolling] = useState(false);

  useEffect(() => {
    fetchCourse();
    if (isAuthenticated) {
      fetchEnrollment();
    }
  }, [id, isAuthenticated]);

  const fetchCourse = async () => {
    try {
      const response = await api.get(`/courses/${id}/`);
      setCourse(response.data);
    } catch (error) {
      console.error('Error fetching course:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchEnrollment = async () => {
    try {
      const response = await api.get(`/courses/${id}/my_enrollment/`);
      setEnrollment(response.data);
    } catch (error) {
      // Not enrolled, that's okay
      setEnrollment(null);
    }
  };

  const handleEnroll = async () => {
    if (!isAuthenticated) {
      navigate('/login');
      return;
    }

    try {
      setEnrolling(true);
      const response = await api.post(`/courses/${id}/enroll/`);
      setEnrollment(response.data);
    } catch (error) {
      alert(error.response?.data?.message || 'Failed to enroll');
    } finally {
      setEnrolling(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading course...</div>;
  }

  if (!course) {
    return <div className="loading">Course not found</div>;
  }

  return (
    <div className="course-detail">
      <div className="container">
        <div className="course-header">
          <div className="course-info">
            <div className="course-badge">
              <span className="level-badge">{course.level}</span>
              <span className="price-badge">
                {course.is_free ? 'Free' : `$${course.price}`}
              </span>
            </div>
            <h1>{course.title}</h1>
            <p className="course-description">{course.description}</p>
            <div className="course-meta-info">
              <span>👨‍🏫 {course.instructor?.username}</span>
              <span>📚 {course.lessons_count || 0} lessons</span>
              <span>⏱️ {course.duration_hours} hours</span>
              <span>👥 {course.enrolled_count || 0} students</span>
            </div>
            {enrollment ? (
              course.lessons && course.lessons.length > 0 ? (
                <Link
                  to={`/courses/${id}/lessons/${course.lessons[0].id}`}
                  className="btn btn-primary btn-large"
                >
                  Continue Learning
                </Link>
              ) : (
                <span className="btn btn-primary btn-large" style={{ opacity: 0.6, cursor: 'not-allowed' }}>
                  No Lessons Available
                </span>
              )
            ) : (
              <button
                onClick={handleEnroll}
                className="btn btn-primary btn-large"
                disabled={enrolling}
              >
                {enrolling ? 'Enrolling...' : 'Enroll Now'}
              </button>
            )}
          </div>
          {course.thumbnail && (
            <div className="course-image">
              <img src={course.thumbnail} alt={course.title} />
            </div>
          )}
        </div>

        <div className="course-content">
          <div className="lessons-section">
            <h2>Course Curriculum</h2>
            {course.lessons && course.lessons.length > 0 ? (
              <div className="lessons-list">
                {course.lessons.map((lesson, index) => (
                  <div key={lesson.id} className="lesson-item">
                    <div className="lesson-number">{index + 1}</div>
                    <div className="lesson-info">
                      <h3>{lesson.title}</h3>
                      <p>{lesson.description}</p>
                      <span className="lesson-duration">⏱️ {lesson.duration_minutes} min</span>
                    </div>
                    {enrollment && (
                      <Link
                        to={`/courses/${id}/lessons/${lesson.id}`}
                        className="btn btn-outline"
                      >
                        Start
                      </Link>
                    )}
                  </div>
                ))}
              </div>
            ) : (
              <p>No lessons available yet.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default CourseDetail;

