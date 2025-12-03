const jobModel = require("../models/jobModel")

const deleteJob = async(req,res) =>{
    try{
        const {jobId} = req.body;
        
        const job = await jobModel.findByIdAndDelete(jobId);

        res.json({
            message : "Job Deleted Successfully!",
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

module.exports = deleteJob ;