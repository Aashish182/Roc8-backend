const mongoose = require('mongoose');

const courseschema = new mongoose.Schema({
    name:String,
    platform:String,
    description:String,
    link:String,
    sendedAt: {
        type: Date,
        default: Date.now,
    },
},{
    timestamps: true
})


const courseModel = mongoose.model("courseschema",courseschema);


module.exports = courseModel;