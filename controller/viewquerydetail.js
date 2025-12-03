const aboutusModel = require("../models/aboutusModel")

const viewquerydetail = async(req,res) =>{
    try{
        const {aboutusId} = req.body;
        
        const query = await aboutusModel.findById(aboutusId);

        res.json({
            data : query,
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

module.exports = viewquerydetail ;