<h1 align="center">🧠 Real-Time Twitter Sentiment Analysis</h1>

<p align="center">
  <strong>Analyze public sentiment on Twitter in real time using Big Data tools.</strong>
</p>

---

<h2>📖 Overview</h2>
<p>
In today’s digital world, social networks are a major source of real-time information. This project focuses on analyzing <strong>public sentiment on Twitter</strong>. Using Big Data tools, it collects, processes, and analyzes live tweets to determine their <strong>emotional tone</strong> (positive, negative, neutral).
</p>

---

<h2>⚙️ System Architecture</h2>
<pre>
   Twitter API  --->  Kafka  --->  Spark Consumer
                                |
                                v
                             MongoDB
                                |
                                v
                      Visualization / Analysis
</pre>

---

<h2>🧩 Technologies Used</h2>
<ul>
  <li>Python – Data collection and processing</li>
  <li>Apache Kafka – Real-time message streaming</li>
  <li>PySpark – Stream processing and sentiment analysis</li>
  <li>MongoDB – NoSQL database for storing analyzed tweets</li>
  <li>Docker – Containerization for reproducible environments</li>
  <li>Tweepy – Access Twitter API</li>
  <li>TextBlob – Sentiment classification</li>
</ul>

---

<h2>🚀 How It Works</h2>
<ol>
  <li><strong>Kafka Producer</strong> fetches live tweets from Twitter using Tweepy.</li>
  <li>Each tweet is sent to a <strong>Kafka topic</strong>.</li>
  <li><strong>PySpark Consumer</strong> listens to the topic, processes tweets, and classifies sentiment using TextBlob.</li>
  <li>Processed data are stored in <strong>MongoDB</strong>.</li>
  <li>The results can be visualized or queried for analysis.</li>
</ol>

---

<h2>🐳 Run with Docker</h2>
<p>Make sure <strong>Docker</strong> and <strong>Docker Compose</strong> are installed.</p>
<pre>
docker-compose up
</pre>
<p>This starts all services: Kafka (KRaft), Spark, MongoDB, Producer (Python), Consumer (PySpark)</p>

---

<h2>📊 Example Output</h2>
<table>
  <thead>
    <tr>
      <th>Tweet</th>
      <th>Sentiment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"I love AI research!"</td>
      <td>Positive</td>
    </tr>
    <tr>
      <td>"This update is terrible."</td>
      <td>Negative</td>
    </tr>
    <tr>
      <td>"It’s just an average day."</td>
      <td>Neutral</td>
    </tr>
  </tbody>
</table>

---

<h2>📁 Project Structure</h2>
<pre>
Project_tweets/
│
├── producer/
│   ├── producer.py
│   └── requirements.txt
│
├── consumer/
│   ├── consumer.py
│   └── requirements.txt
│
├── docker-compose.yml
├── README.md
└── .env
</pre>

---

<h2>👩‍💻 Author</h2>
<ul>
  <li>Fatima-Zahra Boukamar</li>
</ul>

---

<h2>📜 License</h2>
<p>This project is released under the <strong>MIT License</strong>.</p>
