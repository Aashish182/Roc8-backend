const blogModel = require("../models/blogModel")

const viewblogdetail = async(req,res) =>{
    try{
        const {blogId} = req.body;
        
        const blog = await blogModel.findById(blogId);

        res.json({
            data : blog,
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

module.exports = viewblogdetail ;