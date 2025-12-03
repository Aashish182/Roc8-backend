const fetch = require('node-fetch');

const salaryPredict = async (req, res) => {
  try {
    const { experience, education, location, job_title, skills } = req.body;

    const response = await fetch('https://roc8-ml.onrender.com/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        experience,
        education,
        location,
        job_title,
        skills,
      }),
    });

    if (!response.ok) {
      throw new Error(`Python API responded with ${response.status}`);
    }

    const data = await response.json();

    // Return the prediction result
    res.status(200).json({ predicted_salary: data.predicted_salary });

  }catch(err){
    res.status(400).json({
        message: err.message || err,
        error: true,
        success: false
    })
}
};

module.exports = salaryPredict;
