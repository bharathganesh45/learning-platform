import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import './LessonViewer.css';

const LessonViewer = () => {
  const { courseId, lessonId } = useParams();
  const navigate = useNavigate();
  const [course, setCourse] = useState(null);
  const [lesson, setLesson] = useState(null);
  const [progress, setProgress] = useState(null);
  const [loading, setLoading] = useState(true);
  const [currentLessonIndex, setCurrentLessonIndex] = useState(0);

  useEffect(() => {
    fetchCourse();
  }, [courseId]);

  useEffect(() => {
    if (course && lessonId) {
      fetchLesson();
    }
  }, [course, lessonId]);

  const fetchCourse = async () => {
    try {
      const response = await api.get(`/courses/${courseId}/`);
      setCourse(response.data);
      const index = response.data.lessons.findIndex((l) => l.id === parseInt(lessonId));
      setCurrentLessonIndex(index >= 0 ? index : 0);
    } catch (error) {
      console.error('Error fetching course:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchLesson = async () => {
    try {
      const lessonData = course.lessons.find((l) => l.id === parseInt(lessonId));
      setLesson(lessonData);

      // Try to fetch enrollment and progress, but don't fail if not enrolled
      try {
        const enrollmentResponse = await api.get(`/courses/${courseId}/my_enrollment/`);
        const enrollment = enrollmentResponse.data;

        const progressResponse = await api.get(
          `/progress/?enrollment=${enrollment.id}&lesson=${lessonId}`
        );
        if (progressResponse.data.length > 0) {
          setProgress(progressResponse.data[0]);
        }
      } catch (enrollmentError) {
        // User might not be enrolled, that's okay
        console.log('Enrollment not found, continuing without progress data');
      }
    } catch (error) {
      console.error('Error fetching lesson:', error);
    }
  };

  const markAsComplete = async () => {
    try {
      const enrollmentResponse = await api.get(`/courses/${courseId}/my_enrollment/`);
      const enrollment = enrollmentResponse.data;

      await api.post('/progress/', {
        enrollment: enrollment.id,
        lesson: lessonId,
        completed: true,
      });

      setProgress({ ...progress, completed: true });
      alert('Lesson marked as complete!');
    } catch (error) {
      console.error('Error marking lesson complete:', error);
    }
  };

  const navigateToLesson = (newLessonId) => {
    navigate(`/courses/${courseId}/lessons/${newLessonId}`);
  };

  if (loading || !course || !lesson) {
    return <div className="loading">Loading lesson...</div>;
  }

  const nextLesson = course.lessons[currentLessonIndex + 1];
  const prevLesson = course.lessons[currentLessonIndex - 1];

  return (
    <div className="lesson-viewer">
      <div className="lesson-container">
        <div className="lesson-sidebar">
          <h3>Course Content</h3>
          <div className="lessons-nav">
            {course.lessons.map((l, index) => (
              <div
                key={l.id}
                className={`lesson-nav-item ${l.id === parseInt(lessonId) ? 'active' : ''}`}
                onClick={() => navigateToLesson(l.id)}
              >
                <span className="lesson-nav-number">{index + 1}</span>
                <span className="lesson-nav-title">{l.title}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="lesson-content">
          <div className="lesson-header">
            <Link to={`/courses/${courseId}`} className="back-link">
              ← Back to Course
            </Link>
            <h1>{lesson.title}</h1>
            <p className="lesson-description">{lesson.description}</p>
          </div>

          <div className="lesson-video">
            {lesson.video_url ? (
              <iframe
                src={lesson.video_url}
                title={lesson.title}
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
                className="video-player"
              />
            ) : (
              <div className="no-video">
                <p>Video content will be available here</p>
              </div>
            )}
          </div>

          <div className="lesson-text">
            <h2>Lesson Content</h2>
            <div
              className="lesson-text-content"
              dangerouslySetInnerHTML={{ __html: lesson.content || '<p>No content available yet.</p>' }}
            />
          </div>

          <div className="lesson-actions">
            {prevLesson && (
              <button
                onClick={() => navigateToLesson(prevLesson.id)}
                className="btn btn-outline"
              >
                ← Previous Lesson
              </button>
            )}
            <button
              onClick={markAsComplete}
              className="btn btn-primary"
              disabled={progress?.completed}
            >
              {progress?.completed ? '✓ Completed' : 'Mark as Complete'}
            </button>
            {nextLesson ? (
              <button
                onClick={() => navigateToLesson(nextLesson.id)}
                className="btn btn-primary"
              >
                Next Lesson →
              </button>
            ) : (
              <Link to={`/courses/${courseId}`} className="btn btn-primary">
                Finish Course
              </Link>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default LessonViewer;

