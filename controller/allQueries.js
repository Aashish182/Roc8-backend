const aboutusModel = require("../models/aboutusModel");

async function allQueries(req,res) {
    try{
        const allQueries = await aboutusModel.find()

        res.json({
            message: "All Query Details",
            data: allQueries,
            success: true,
            error: false
        })
    } catch(err){
        res.json({
            message: err.message || err,
            error: true,
            success: false,
        })
    }
}

module.exports = allQueries;