const axios = require('axios');
const Airtable = require('airtable');

// Замініть ці змінні на власні значення
const repositoryOwner = 'SAHavrylova';
const repositoryName = 'Course';
const githubToken = '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';
const labelName = 'bug';

// Створення заголовку авторизації з токеном GitHub
const headers = {
  'Authorization': `Bearer ${githubToken}`
};

// URL запиту до API GitHub для отримання пул-реквестів з певним лейблом
const url = `https://api.github.com/repos/${repositoryOwner}/${repositoryName}/pulls?state=all&labels=${labelName}`;

// Виконання запиту GET до GitHub API
axios.get(url, { headers })
  .then(response => {
    // Обробка результатів запиту
    const pullRequests = response.data;
    
    // Підключення до бази даних Airtable
    const airtable = new Airtable({ apiKey: 'patZdWixEr0glJSj3.b2b92bf903678c34343d82520ea9b2cedec0dffd5d49d7a6a915980d3c37b33b' })
      .base('appS45wKb3a7fXzHi')('Table'); // Замініть на свій ідентифікатор бази та таблиці

    // Запис результатів у таблицю Airtable
    pullRequests.forEach(pr => {
      const prUrl = pr.html_url;  // URL пул-реквесту
      const prTitle = pr.title;  // Назва пул-реквесту
      airtable.create({ 'Title': prTitle, 'URL': prUrl }, (err, record) => {
        if (err) {
          console.error('Помилка при записі в Airtable:', err);
        } else {
          console.log('Запис створено в Airtable:', record.getId());
        }
      });
    });
  })
  .catch(error => {
    console.error('Не вдалося отримати дані. Помилка:', error);
  });
