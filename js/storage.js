/**
 * Storage & Local Data Persistence Manager
 * Handles offline caching of user progress, question attempts, completed topics,
 * and exam simulation history via localStorage and JSON export/import.
 */

const STORAGE_KEYS = {
  COMPLETED_TOPICS: 'pem_completed_topics',
  QUESTION_PROGRESS: 'pem_question_progress',
  EXAM_HISTORY: 'pem_exam_history',
  SETTINGS: 'pem_settings',
  LAST_ACTIVE_TOPIC: 'pem_last_active_topic'
};

const StorageManager = {
  // Topics Completion
  getCompletedTopics() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.COMPLETED_TOPICS);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error('Failed to read completed topics', e);
      return [];
    }
  },

  isTopicCompleted(topicId) {
    const list = this.getCompletedTopics();
    return list.includes(topicId);
  },

  toggleTopicCompleted(topicId) {
    let list = this.getCompletedTopics();
    if (list.includes(topicId)) {
      list = list.filter(id => id !== topicId);
    } else {
      list.push(topicId);
    }
    localStorage.setItem(STORAGE_KEYS.COMPLETED_TOPICS, JSON.stringify(list));
    return list.includes(topicId);
  },

  // Questions Attempted
  getQuestionProgress() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.QUESTION_PROGRESS);
      return data ? JSON.parse(data) : { attempted: {}, correctCount: 0, wrongCount: 0 };
    } catch (e) {
      return { attempted: {}, correctCount: 0, wrongCount: 0 };
    }
  },

  saveQuestionAttempt(qId, selectedAnswer, isCorrect) {
    const prog = this.getQuestionProgress();
    const prev = prog.attempted[qId];

    prog.attempted[qId] = {
      selected: selectedAnswer,
      isCorrect: isCorrect,
      timestamp: Date.now()
    };

    // Re-tally
    let correct = 0;
    let wrong = 0;
    Object.values(prog.attempted).forEach(item => {
      if (item.isCorrect) correct++;
      else wrong++;
    });
    prog.correctCount = correct;
    prog.wrongCount = wrong;

    localStorage.setItem(STORAGE_KEYS.QUESTION_PROGRESS, JSON.stringify(prog));
    return prog;
  },

  // Exam Simulation History
  getExamHistory() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.EXAM_HISTORY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  },

  saveExamResult(resultRecord) {
    const history = this.getExamHistory();
    const newEntry = {
      ...resultRecord,
      id: 'exam-' + Date.now(),
      date: new Date().toLocaleDateString('en-GB')
    };
    history.unshift(newEntry);
    localStorage.setItem(STORAGE_KEYS.EXAM_HISTORY, JSON.stringify(history));
    return history;
  },

  updateLatestExamResult(updatedRecord) {
    const history = this.getExamHistory();
    if (history.length > 0) {
      history[0] = {
        ...history[0],
        ...updatedRecord
      };
      localStorage.setItem(STORAGE_KEYS.EXAM_HISTORY, JSON.stringify(history));
    }
    return history;
  },

  // Theme Settings
  getTheme() {
    return localStorage.getItem('pem_theme') || 'light';
  },

  setTheme(theme) {
    localStorage.setItem('pem_theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
  },

  // Export Data for Backup
  exportAllDataJSON() {
    const backup = {
      completedTopics: this.getCompletedTopics(),
      questionProgress: this.getQuestionProgress(),
      examHistory: this.getExamHistory(),
      exportedAt: new Date().toISOString()
    };
    return JSON.stringify(backup, null, 2);
  },

  // Import Data from JSON with strict schema validation
  importDataJSON(jsonString) {
    try {
      if (!jsonString || typeof jsonString !== 'string') {
        return { success: false, error: 'Empty or invalid file content' };
      }
      const parsed = JSON.parse(jsonString);
      if (typeof parsed !== 'object' || parsed === null) {
        return { success: false, error: 'JSON root must be an object' };
      }

      let restoredAny = false;

      // 1. Validate and restore completed topics
      if (parsed.completedTopics) {
        if (Array.isArray(parsed.completedTopics)) {
          // ensure array elements are strings
          const validTopics = parsed.completedTopics.filter(t => typeof t === 'string');
          localStorage.setItem(STORAGE_KEYS.COMPLETED_TOPICS, JSON.stringify(validTopics));
          restoredAny = true;
        } else {
          return { success: false, error: 'Invalid completedTopics format: expected an array' };
        }
      }

      // 2. Validate and restore question progress
      if (parsed.questionProgress) {
        if (typeof parsed.questionProgress === 'object' && parsed.questionProgress !== null) {
          const qp = parsed.questionProgress;
          const safeQP = {
            attempted: typeof qp.attempted === 'object' && qp.attempted !== null ? qp.attempted : {},
            correctCount: typeof qp.correctCount === 'number' ? qp.correctCount : 0,
            wrongCount: typeof qp.wrongCount === 'number' ? qp.wrongCount : 0
          };
          localStorage.setItem(STORAGE_KEYS.QUESTION_PROGRESS, JSON.stringify(safeQP));
          restoredAny = true;
        } else {
          return { success: false, error: 'Invalid questionProgress format: expected an object' };
        }
      }

      // 3. Validate and restore exam history
      if (parsed.examHistory) {
        if (Array.isArray(parsed.examHistory)) {
          localStorage.setItem(STORAGE_KEYS.EXAM_HISTORY, JSON.stringify(parsed.examHistory));
          restoredAny = true;
        } else {
          return { success: false, error: 'Invalid examHistory format: expected an array' };
        }
      }

      if (!restoredAny) {
        return { success: false, error: 'File contains no recognizable Python Exam Master progress data' };
      }

      return { success: true };
    } catch (e) {
      return { success: false, error: 'Malformed JSON file: ' + e.message };
    }
  }
};

// Initialize Theme on load
(function() {
  const currentTheme = StorageManager.getTheme();
  document.documentElement.setAttribute('data-theme', currentTheme);
})();

