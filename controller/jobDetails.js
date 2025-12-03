const jobModel = require("../models/jobModel");

const jobDetailsController = async(req,res) => {
    try{
        const job = await jobModel.find().sort({ createdAt : -1 });

        res.json({
            data: job,
            error: false,
            success: true,
            message: " Job details "
        })

    }catch(err){
        res.status(400).json({
            message: err.message || err,
            error: true,
            success: false
        })
    }
}

module.exports = jobDetailsController;