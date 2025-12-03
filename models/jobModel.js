const mongoose = require('mongoose');
const schema = mongoose.Schema;

const jobSchema = new mongoose.Schema({
    title: String,
    growth: Number,
    demand: Number,
    category: String,
    AddedAt: {
        type: Date,
        default: Date.now,
    },
},{
    timestamps: true
})

const jobModel = mongoose.model("job",jobSchema);


module.exports = jobModel;