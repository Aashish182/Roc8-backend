
const blogModel = require("../models/blogModel")

async function updateBlog(req,res) {
    try{
        const sessionUser = req.userId
        const { blogId, title, content } = req.body;
        const payload = {
            ...( title && { title}),
            ...( content && { content}),
        }

        const updatedBlog = await blogModel.findByIdAndUpdate(blogId, payload, {
            new: true, 
            runValidators: true 
        });

        res.json({
            data: updatedBlog,
            message: "Blog Updated",
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

module.exports = updateBlog;