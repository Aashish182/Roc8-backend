
const feedbackModel = require("../models/feedbackModel");


async function feedback(req,res) {
    try{
        const { feedback } = req.body;

        const userData = new feedbackModel(req.body);
        const saveFeedback = await userData.save()

        res.status(201).json({
            data: saveFeedback,
            success:true,
            error:false,
            message: "Thank You For Your Feedback"
        })

    }catch(err){
        res.json({
            message: err.message || err,
            error: true,
            success: false,
        })
    }
}

module.exports = feedback;