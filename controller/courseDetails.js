const uploadCampiagnPermission = require("../helper/permission");
const courseModel = require("../models/courseModel")


async function courseDetails(req,res) {
    try{
        const course = await courseModel.find().sort({ createdAt : -1 });

        res.json({
            data: course,
            error: false,
            success: true,
            message: " Course details "
        })

    }catch(err){
        res.status(400).json({
            message: err.message || err,
            error: true,
            success: false
        })
    }
}

module.exports = courseDetails;