const feedbackModel = require("../models/feedbackModel");

const userFeedback = async(req,res) =>{
    try{
        const {userId} = req.body;
        
        const userfeedbackdetail = await feedbackModel.find({creator: userId});
        
        if (!userfeedbackdetail || userfeedbackdetail.length === 0) {
            return res.json({
                data: [],
                message: "No Details found for this user",
                success: true,
                error: false
            });
        }

        res.json({
            data : userfeedbackdetail,
            message : "ok",
            success : true,
            error : false
        })

    } catch(err) {
        res.json({
            message: err?.message || err,
            error : true,
            success : false
        })
    }
}

module.exports = userFeedback ;