const feedbackModel = require("../models/feedbackModel");

const feedbackDetails = async(req,res) => {
    try{
        const feedback = await feedbackModel.find().sort({ createdAt : -1 });

        res.json({
            data: feedback,
            error: false,
            success: true,
            message: " Feedback details "
        })

    }catch(err){
        res.status(400).json({
            message: err.message || err,
            error: true,
            success: false
        })
    }
}

module.exports = feedbackDetails;