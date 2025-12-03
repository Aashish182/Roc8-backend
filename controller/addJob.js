
const jobModel = require("../models/jobModel");


async function addJob(req,res) {
    try{

        const sessioUserId = req.userId;

        const { title, growth, demand, category } = req.body;

        if(!title){
            throw new Error("Please Provide Title")
        }
        if(!growth){
            throw new Error("Please Provide Growth")
        }
        if(!demand){
            throw new Error("Please Provide Demand")
        }
        if(!category){
            throw new Error("Please Provide Category")
        }

        const jobData = new jobModel(req.body);
        const saveJob = await jobData.save()

        res.status(201).json({
            data: saveJob,
            success:true,
            error:false,
            message: "Job Trend Added Successfully! "
        })

    }catch(err){
        res.json({
            message: err.message || err,
            error: true,
            success: false,
        })
    }
}

module.exports = addJob;